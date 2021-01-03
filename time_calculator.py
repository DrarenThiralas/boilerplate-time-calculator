weekdayList = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

class Time():

	def __init__(self, timestring, weekday = None):
		hmString, ampmString = timestring.split(" ")
		hourString, minuteString = hmString.split(":")
		self.days = 0
		self.startday = weekday.lower() if weekday else None
		self.weekday = self.startday
		self.hours = int(hourString)
		if ampmString == "PM":
			self.hours += 12
		self.minutes = int(minuteString)
		self.__normalizeTime()

	def __normalizeTime(self):
		self.hours += int(self.minutes/60)
		self.minutes = self.minutes%60
		self.days += int(self.hours/24)
		self.hours = self.hours%24
		if self.startday is not None:
			weekdayIndex = weekdayList.index(self.startday.lower())
			toAddIndex = self.days%7
			if weekdayIndex + toAddIndex > 6:
				self.weekday = weekdayList[weekdayIndex + toAddIndex - 7]
			else:
				self.weekday = weekdayList[weekdayIndex + toAddIndex]

	def get(self):
		returnString = ""
		minuteString = str(self.minutes)
		if self.minutes < 10:
			minuteString = "0"+minuteString

		if self.hours > 12:
			returnString = str(self.hours-12)+":"+minuteString+" PM"
		elif self.hours == 12:
			returnString = str(self.hours)+":"+minuteString+" PM"
		elif self.hours == 0:
			returnString = "12:"+minuteString +" AM"
		else:
			returnString = str(self.hours)+":"+minuteString+" AM"

		if self.startday is not None:
			returnString = returnString + ", " + self.weekday[0].upper()+self.weekday[1:]

		if self.days > 0:
			if self.days > 1:
				returnString = returnString + " (" + str(self.days) + " days later)"
			else:
				returnString = returnString + " (next day)"

		return returnString

	def toTimestring(self, extraHours, extraMinutes):
		returnString = str(self.hours+extraHours)+":"+str(self.minutes+extraMinutes)+" AM"
		return returnString

	def add(self, addstring):
		addHours, addMinutes = addstring.split(":")
		addHours, addMinutes = int(addHours), int(addMinutes)
		newTime = Time(self.toTimestring(addHours, addMinutes), self.startday)
		return newTime

def add_time(start, duration, weekday = None):


	currentTime = Time(start, weekday)
	newTime = currentTime.add(duration)
	new_time = newTime.get()


	return new_time