# This function returns the minimum number of lights that should be fixed in order to get K lights fixed consecutively 
def lights_required_fix(no_lights : int, no_lights_required_work : int, no_broken_lights : int, broken_lights_data : list):
	# This list represents the data for all the lights, True for working lights, False for broken lights
	lights_data = [True for _ in range(no_lights + 1)]
	for _ in broken_lights_data:
		lights_data[_] = False

	# Minimum number of lights required to be fixed
	min_lights_required = no_lights
	
	psum = [] # The number of broken lights before light i
	for _ in range(no_lights + 1):
		if psum == []:
			psum.append(0)
		elif lights_data[_] == False:
			psum.append(psum[_ - 1] + 1)
		else:
			psum.append(psum[_ - 1])
		if _ >= no_lights_required_work:
			min_lights_required = min(min_lights_required, psum[_] - psum[_ - no_lights_required_work])

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
