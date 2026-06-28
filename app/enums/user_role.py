from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"          # полный доступ
    IT = "it"                # инженер
    MANAGER = "manager"      # руководитель
    OPERATOR = "operator"    # оператор
    AUDITOR = "auditor"      # аудит
    VIEWER = "viewer"        # только просмотр
    USER = "user"            # обычный пользователь
