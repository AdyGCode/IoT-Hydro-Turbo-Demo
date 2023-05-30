import threading

# ...

@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()
