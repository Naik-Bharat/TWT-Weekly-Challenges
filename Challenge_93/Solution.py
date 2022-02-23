# This function returns the minimum number of lights that should be fixed in order to get K lights fixed consecutively 
def lights_required_fix(no_lights : int, no_lights_required_work : int, no_broken_lights : int, broken_lights_data : list):
	# This list represents the data for all the lights, True for working lights, False for broken lights
	lights_data = [True for _ in range(no_lights)]
	for _ in broken_lights_data:
		lights_data[_ - 1] = False

	# Minimum number of lights required to be fixed
	min_lights_required = no_lights

	# for every possible light queue, the starting ligths index
	for light_index in range(no_lights - no_broken_lights):
		# Number of lights to fix for this case if all lights need to be fixed in this queue
		lights_to_fix = lights_data[light_index : light_index + no_lights_required_work].count(False)
		if lights_to_fix < min_lights_required:
			min_lights_required = lights_to_fix

	return min_lights_required


# This function returns a list of int values of all the values in the list
str_to_int = lambda x: [int(_) for _ in x]

def main():	
	T = int(input())
	for _ in range(T):
		no_lights, no_lights_required_work, no_broken_lights = str_to_int(str(input()).split())
		broken_lights_data = str_to_int(str(input()).split())
		
		print(lights_required_fix(no_lights, no_lights_required_work, no_broken_lights, broken_lights_data))


main()
