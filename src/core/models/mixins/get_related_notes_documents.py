# -*- coding: utf-8 -*-#

from core.utils.developments.debugging_print_object import DebuggingPrint


class BWGetRelatedNotesAndDocuments:
    """
    A mixin class for retrieving related notes and documents.

    Methods:
        related_for_job(self) -> dict: Returns an empty dictionary.
        related_for_clients(self) -> dict: Retrieves related notes and documents for clients.
        get_all_related_notes_and_documents(self) -> dict: Retrieves related notes and documents based on the value of `RELATED_ITEM_ID`.

    """

    def related_for_job(self) -> dict:
        """
        Returns an empty dictionary.
        """
        try:
            from document.models import Document
            from task.models import TaskProxy
            from note.models import Note

            data = {}

            return data
        except Exception as ex:
            DebuggingPrint.print_exception()

    def related_for_clients(self) -> dict:
        """
        Retrieves related notes and documents for clients.
        """
        try:
            from document.models import Document
            from task.models import TaskProxy
            from note.models import Note

            data = {"notes": Note.objects.none(), "documents": Document.objects.none()}
            if hasattr(self, "notes"):
                data.update({"notes": self.notes.prefetch_related()})
            if hasattr(self, "documents"):
                data.update({"documents": self.documents.prefetch_related()})
            if hasattr(self, "jobs"):
                if self.jobs.prefetch_related().exists() is True:
                    for job in self.jobs.prefetch_related():
                        if hasattr(job, "notes"):
                            if job.notes.prefetch_related().exists() is True:
                                data["notes"] |= job.notes.prefetch_related()
                        if hasattr(job, "documents"):
                            if job.documents.prefetch_related().exists() is True:
                                data["documents"] |= job.documents.prefetch_related()
                        if hasattr(job, "tasks"):
                            for task in job.tasks.prefetch_related():
                                if hasattr(task, "notes"):
                                    data["notes"] |= task.notes.prefetch_related()
                                if hasattr(task, "documents"):
                                    data["documents"] |= task.documents.prefetch_related()

            # DebuggingPrint.pprint(data)
            return data
        except Exception as ex:
            DebuggingPrint.print_exception()

    def get_all_related_notes_and_documents(self) -> dict:
        """
        Retrieves related notes and documents based on the value of `RELATED_ITEM_ID`.
        """
        try:
            if self.RELATED_ITEM_ID == "client":
                return self.related_for_clients()
        except Exception as ex:
            DebuggingPrint.print_exception()
