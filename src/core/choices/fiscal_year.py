from django.db import models


class FiscalYearEnum(models.TextChoices):
    # __empty__ = "---"
    Y2019 = "2019", "2019"
    Y2020 = "2020", "2020"
    Y2021 = "2021", "2021"
    Y2022 = "2022", "2022"
    Y2023 = "2023", "2023"
    Y2024 = "2024", "2024"
    Y2025 = "2025", "2025"
