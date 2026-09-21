
class UserService:

    def create_user(self, name, phone, country):
        if not name:
            raise ValueError("Name is required.")

        if not phone:
            raise ValueError("Phone number is required.")

        if not country:
            raise ValueError("Country is required.")

        return {
            "name": name,
            "phone": phone,
            "country": country
        }

    def get_user(self, user_id):
        if not user_id:
            raise ValueError("User ID is required.")

        # Database connection will be added later
        return {
            "user_id": user_id
        }
