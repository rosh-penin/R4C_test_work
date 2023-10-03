import xlsxwriter
from io import BytesIO


def worksheet_init(workbook: xlsxwriter.Workbook, modelname: str) -> None:
    """
    Инициализирует новый лист в книге excel.
    У каждой модели роботов свой лист.
    """
    current_worksheet = workbook.add_worksheet(modelname)
    current_worksheet.set_column('A:B', 10)
    current_worksheet.set_column('C:C', 25)
    c_format = workbook.add_format({'border': 2, 'align': 'center'})
    current_worksheet.write_row(
        0,
        0,
        ('Модель', 'Версия', 'Количество за неделю'),
        c_format
    )


def get_excel_file_from_queryset(queryset):
    """
    Создает файл excel по данным из queryset.
    Данные должны быть отсортированы для корректной работы.
    """
    result = BytesIO()
    workbook = xlsxwriter.Workbook(result)
    c_format = workbook.add_format({'border': 1, 'align': 'center'})
    row_number: int = 1
    for item in queryset:
        model = item['model']
        if model not in workbook.sheetnames:
            row_number = 1
            worksheet_init(workbook, model)
        workbook.sheetnames[model].write_row(
            row_number,
            0,
            (model, item['version'], item['count']),
            c_format
        )
        row_number += 1
    workbook.close()
    result.seek(0)
    return result
