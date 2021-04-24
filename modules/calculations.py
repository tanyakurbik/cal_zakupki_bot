from modules.days_off_utils import DaysOff

days_off = DaysOff(path_to_days_off="days_off.yaml")


def e_store(start_date):
    preparation = days_off.plus_n_workdays(start_date, 5)
    publication = days_off.plus_n_workdays(preparation, 3)
    conclusion = days_off.plus_n_workdays(publication, 2)
    result = {
        "Дата подготовки документов ОГЗ": preparation,
        "Дата окончания подачи заявок": publication,
        "Дата заключения контракта": conclusion,
    }
    return result


def auction_ogz(start_date):
    preparation = days_off.plus_n_workdays(start_date, 5)
    publication = days_off.plus_n_calendar_days(preparation, 7)
    summarizing = days_off.plus_n_workdays(publication, 3)
    conclusion = days_off.plus_n_calendar_days(summarizing, 10)
    result = {
        "Дата подготовки документов ОГЗ": preparation,
        "Дата окончания подачи заявок": publication,
        "Дата подведения итогов": summarizing,
        "Дата заключения контракта": conclusion,
    }
    return result


def contest_ogz(start_date):
    preparation = days_off.plus_n_workdays(start_date, 5)
    publication = days_off.plus_n_workdays(preparation, 15)
    summarizing = days_off.plus_n_workdays(publication, 4)
    conclusion = days_off.plus_n_calendar_days(summarizing, 10)
    result = {
        "Дата подготовки документов ОГЗ": preparation,
        "Дата окончания подачи заявок": publication,
        "Дата подведения итогов": summarizing,
        "Дата заключения контракта": conclusion,
    }
    return result


def auction_kgz(start_date):
    preparation = days_off.plus_n_workdays(start_date, 5)
    preparation_kgz = days_off.plus_n_workdays(preparation, 10)
    publication = days_off.plus_n_calendar_days(preparation_kgz, 7)
    summarizing = days_off.plus_n_workdays(publication, 5)
    conclusion = days_off.plus_n_calendar_days(summarizing, 10)
    result = {
        "Дата подготовки документов ОГЗ": preparation,
        "Дата завершения рассмотрения документов КГЗ": preparation_kgz,
        "Дата окончания подачи заявок": publication,
        "Дата подведения итогов": summarizing,
        "Дата заключения контракта": conclusion,
    }
    return result


def contest_kgz(start_date):
    preparation = days_off.plus_n_workdays(start_date, 5)
    preparation_kgz = days_off.plus_n_workdays(preparation, 10)
    publication = days_off.plus_n_workdays(preparation_kgz, 15)
    summarizing = days_off.plus_n_workdays(publication, 7)
    conclusion = days_off.plus_n_calendar_days(summarizing, 10)
    result = {
        "Дата подготовки документов ОГЗ": preparation,
        "Дата завершения рассмотрения документов КГЗ": preparation_kgz,
        "Дата окончания подачи заявок": publication,
        "Дата подведения итогов": summarizing,
        "Дата заключения контракта": conclusion,
    }
    return result
