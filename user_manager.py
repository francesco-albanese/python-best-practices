import re
from typing import Dict, Any

class UserRepository:
    def __init__(self):
        self.users: Dict[int, Dict[str, Any]] = {}
        self.user_id = 1

    def save(self, user_data: Dict[str, Any]) -> None:
        self.users[self.user_id] = user_data
        self.user_id += 1

    def get_all(self) -> Dict[int, Dict[str, Any]]:
        return self.users

class EmailValidator:
    @staticmethod
    def validate(email: str) -> bool:
        """Validate email format using regex."""
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

class PasswordValidator:
    @staticmethod
    def validate(password: str, min_length: int = 8) -> bool:
        """Validate password strength."""
        return len(password) >= min_length

class EmailService:
    def send_welcome_email(self, email: str) -> None:
        """Send a welcome email to the user."""
        print(f"Sending welcome email to {email}")

class UserActivityLogger:
    def log_creation(self, user_id: int) -> None:
        """Log user creation activity."""
        print(f"User with ID {user_id} created.")

class UserService:
    def __init__(self, user_repository: UserRepository, email_service: EmailService, user_activity_logger: UserActivityLogger):
        self.user_repository = user_repository
        self.email_service = email_service
        self.user_activity_logger = user_activity_logger

    def create_user(self, email: str, password: str) -> int:
        """Orchestrates user creation."""
        if not EmailValidator.validate(email):
            raise ValueError("Invalid email format")
        if not PasswordValidator.validate(password):
            raise ValueError("Password is not strong enough")

        user_data = {"email": email, "password": password}
        self.user_repository.save(user_data)
        self.email_service.send_welcome_email(email)
        self.user_activity_logger.log_creation(self.user_repository.user_id)
        return self.user_repository.user_id

class UserReportGenerator:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def generate_report(self) -> None:
        """Generate a report of all users."""
        users = self.user_repository.get_all()
        print("--- User Report ---")
        for user_id, user_data in users.items():
            print(f"User ID: {user_id}, Email: {user_data['email']}")
        print("--- End of Report ---")


if __name__ == "__main__":
    user_id = 1
    user_repository = UserRepository(user_id)
    email_service = EmailService()
    user_activity_logger = UserActivityLogger()
    user_service = UserService(user_repository, email_service, user_activity_logger)
    
    user_service.create_user("test@example.com", "password123")

    user_report_generator = UserReportGenerator(user_repository)
    user_report_generator.generate_report()
    
    print(f"User ID: {user_id}")
