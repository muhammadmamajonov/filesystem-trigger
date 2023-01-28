import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers.polling import PollingObserver

class OnMyWatch:
	# Set the directory on watch
	watchDirectory = "files"

	def __init__(self):
		self.observer = PollingObserver()

	def run(self):
		event_handler = Handler()
		self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
		self.observer.start()
		try:
			while True:
				time.sleep(5)
		except:
			self.observer.stop()
			print("Observer Stopped")

		self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        """You can write your code here"""
        if event.is_directory:
            print(f"Directroy {event.event_type}: ", event.src_path)
        else:
            print(f"File {event.event_type}: ", event.src_path)
		    

		

if __name__ == '__main__':
	watch = OnMyWatch()
	watch.run()



