from typing import Annotated
from fastapi import APIRouter, File
from fastapi.responses import FileResponse

from src.report.reports import build_new_report

router = APIRouter(prefix='/report', tags=['Report'])


@router.post('/', summary='Загрузка отчета')
def upload(file: Annotated[bytes, File()]):
    '''Загрузите excel файл(Исчисления НДФЛ).
    На выходе получите отчет, который можно будет скачать.'''
    try:
        file_path = 'rept_header.xlsx'
        build_new_report(file, f'../../{file_path}')
        return FileResponse(file_path, filename=file_path, media_type='multipart/form-data')

    except ValueError:
        return {'status': 'Error',
                'message': 'The file format must be .xlsx'}
    except Exception as er:
        return {'status': 'Error',
                'message': er}