"""Management command to safely re-encrypt legacy or old-key production database records."""

from __future__ import annotations

from django.core.management.base import BaseCommand

from client_account.models import ClientAccount
from core.crypto.engine import VERSION_PREFIX_V2, CryptoEngine
from staff_briefcase.models.accounts.staff_accounts import StaffAccounts


class Command(BaseCommand):
    help = "Re-encrypts legacy production credentials to the latest ENCRYPT_KEY and v2$ format."

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Inspect records without saving changes to the database.",
        )
        parser.add_argument(
            "--batch-size",
            type=int,
            default=100,
            help="Batch size for processing database records.",
        )

    def handle(self, *args, **options):
        dry_run = options["dry_run"]
        batch_size = options["batch_size"]

        self.stdout.write(
            self.style.SUCCESS(
                f"Starting re-encryption scan (dry_run={dry_run}, batch_size={batch_size})..."
            )
        )

        updated_ca = 0
        failed_ca = 0

        # 1. Process ClientAccount records
        ca_qs = ClientAccount.objects.all()
        for account in ca_qs:
            raw = account.account_password
            if raw and not raw.startswith(VERSION_PREFIX_V2):
                decrypted = CryptoEngine.decrypt(raw)
                if decrypted:
                    if not dry_run:
                        account.account_password = decrypted
                        account.save(update_fields=["account_password"])
                    updated_ca += 1
                else:
                    failed_ca += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"ClientAccount records: {updated_ca} upgraded, {failed_ca} failed decryption."
            )
        )

        # 2. Process StaffAccounts records
        updated_sa = 0
        failed_sa = 0
        sa_qs = StaffAccounts.objects.all()
        for account in sa_qs:
            raw = account.password
            if raw and not raw.startswith(VERSION_PREFIX_V2):
                decrypted = CryptoEngine.decrypt(raw)
                if decrypted:
                    if not dry_run:
                        account.password = decrypted
                        account.save(update_fields=["password"])
                    updated_sa += 1
                else:
                    failed_sa += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"StaffAccounts records: {updated_sa} upgraded, {failed_sa} failed decryption."
            )
        )
