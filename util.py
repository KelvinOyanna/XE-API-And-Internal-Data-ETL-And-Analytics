from datetime import datetime


def check_last_updated(json_record, response_data):
        last_updated = datetime.strptime(json_record[-1].get('timestamp'), '%Y-%m-%dT%H:%M:%SZ').date()
        if (datetime.strptime(response_data.get('timestamp'), '%Y-%m-%dT%H:%M:%SZ').date()) != last_updated:
            return True
        else:
            return False
