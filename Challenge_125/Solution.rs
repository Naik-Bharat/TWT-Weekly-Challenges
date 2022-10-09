use std::io;

fn main(){
	let t: u32;
	let mut t_input = String::new();
	io::stdin().read_line(&mut t_input).expect("failed to read input!");
	t = t_input.trim().parse().unwrap();
	for _ in 0..t{
		// taking inputs
		let mut case_input = String::new();
		io::stdin().read_line(&mut case_input).expect("failed to read input!");
		let mut _v: Vec<&str> = case_input.split(" ").collect();
		let n: u32 = _v[0].trim().parse().unwrap();    // number of pokemons
		let sum: u32 = _v[1].trim().parse().unwrap();    // sum of pokemons
		let mut arr: Vec<u32> = vec!(0; n as usize);
		let mut array_input = String::new();
		io::stdin().read_line(&mut array_input).expect("failed to read input!");
		_v = array_input.split(" ").collect();
		for i in 0..n{
			arr[i as usize] = _v[i as usize].trim().parse().unwrap();
		}

		let mut count: u32 = 0;    // count of distinct subarrays of required sum
		let mut start: u32 = 0;    // starting index of current subarray
		let mut end: u32 = 0;    // ending index of current subarray
		let mut current_sum: u32 = arr[0];
		while end < n{
			if current_sum == sum{
				count += 1;
			}
			if current_sum < sum{
				end += 1;
				if end == n{
					break;
				}
				current_sum += arr[end as usize];
			}
			else{
				current_sum -= arr[start as usize];
				start += 1;
			}
		}
		println!("{}", count);
	}
}