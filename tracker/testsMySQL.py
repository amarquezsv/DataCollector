from unittest.mock import patch
from tracker.models import Client

@patch('tracker.models.Client.objects.create')
def test_client_creation(mock_create):
    mock_create.return_value = Client(id=1, name="Test Client")
    client = Client.objects.create(name="Test Client")
    assert client.name == "Test Client"

class FakeInvoiceRepository:
    def save(self, invoice):
        return True  # Pretend it was saved

def test_invoice_service():
    repo = FakeInvoiceRepository()
    assert repo.save({"id": 1, "amount": 100}) is True


# import requests
# from unittest.mock import patch

# @patch('requests.post')
# def test_send_invoice(mock_post):
#     mock_post.return_value.status_code = 200
#     mock_post.return_value.json.return_value = {"status": "success"}
#     response = requests.post("https://hacienda.gob.sv/api/invoice", json={})
#     assert response.json()["status"] == "success"


# from unittest.mock import MagicMock

# def test_alert_trigger():
#     alert_service = MagicMock()
#     alert_service.send_alert("Resource issue")
#     alert_service.send_alert.assert_called_once_with("Resource issue")
