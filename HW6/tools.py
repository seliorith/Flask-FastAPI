from passlib.context import CryptContext

__all__ = ['get_password_hash']
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # создание экземпляра CryptContext, который определяет алгоритмы хеширования, в данном случае используется bcrypt


def __validate_password(password) -> str:  # принимает пароль и проверяет его на соответствие определенным критериям безопасности
    """Валидатор пароля"""
    if len(password) < 8:
        raise ValueError('Пароль должен содержать как минимум 8 символов')
    if not any(char.isdigit() for char in password):
        raise ValueError('Пароль должен содержать как минимум одну цифру')
    if not any(char.isupper() for char in password):
        raise ValueError('Пароль должен содержать как минимум одну заглавную букву')
    return password


async def get_password_hash(password: str) -> str:
    """ Генерирует хеш заданного пароля."""
    __validate_password(password)
    return pwd_context.hash(password)