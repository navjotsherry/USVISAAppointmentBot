import json
from time import sleep
from utils.compareDates import compareDates

def interceptor(request,response):
    if request.url.startswith('https://ais.usvisa-info.com/en-ca/niv/schedule/60598244/appointment/days/94'):
            try:
            # Wait and retry mechanism
                for _ in range(10):  # Retry up to 10 times
                    if response is not None:
                        break
                    sleep(5)  # Wait for 0.5 seconds before retrying
                
                if response is None:
                    print("Response not available for request:", request.url)
                    return

                # Write response body to a file
                print( request.url)
                print(response)
                f= open("AvailableTorontoAppointments.txt", "a")
                f.write("Response Body: " + str(response.body))
                f.close()
                json_response = json.loads(response.body)
                if len(json_response) == 0:
                    print("No available appointments")
                    return
                print(json_response[0]['date'])
                first_available_date = json_response[0]['date']
                current_appointment = request['current_appointment']
                compareDates(first_available_date, current_appointment)

                print("Response body written to response_body.txt")

            except AttributeError as e:
                print("Error handling request:", e)
                # Wait for the request to be processed