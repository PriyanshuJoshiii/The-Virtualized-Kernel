import threading
import time

# --- The two resources ---
# Imagine this is the can of paint
paint_lock = threading.Lock()
# Imagine this is the ladder
ladder_lock = threading.Lock()

# --- The two painters (threads) ---

def painter_bob():
    print("Bob (Thread 1): Trying to get the ladder...")
    ladder_lock.acquire()
    print("Bob (Thread 1): Got the ladder! ✅")

    # This sleep is important! It gives Alice time to grab the paint.
    time.sleep(1)

    print("Bob (Thread 1): Now trying to get the paint...")
    paint_lock.acquire() # This is where Bob will get stuck and wait forever
    print("Bob (Thread 1): Got the paint!") # This line will never be reached

    # Release the resources (this will never happen)
    paint_lock.release()
    ladder_lock.release()

def painter_alice():
    print("Alice (Thread 2): Trying to get the paint...")
    paint_lock.acquire()
    print("Alice (Thread 2): Got the paint! ✅")

    time.sleep(1)

    print("Alice (Thread 2): Now trying to get the ladder...")
    ladder_lock.acquire() # This is where Alice will get stuck and wait forever
    print("Alice (Thread 2): Got the ladder!") # This line will never be reached

    # Release the resources (this will never happen)
    ladder_lock.release()
    paint_lock.release()


# --- Start the demonstration ---
if __name__ == "__main__":
    print("--- Starting Deadlock Demonstration ---")
    
    # Create and start the two painter threads
    thread_bob = threading.Thread(target=painter_bob)
    thread_alice = threading.Thread(target=painter_alice)

    thread_bob.start()
    thread_alice.start()

    # Wait for the threads to finish (they never will)
    thread_bob.join()
    thread_alice.join()

    # This final message will never be printed because the program is stuck
    print("--- Demonstration Finished ---")