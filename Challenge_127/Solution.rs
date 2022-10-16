use std::io;

// This function returns the number of ways to get to n
fn no_ways(n: u32, d: u32, cache: &mut [u32; 1e5 as usize]) -> u32{
	let mut output: u32 = 0;
	for roll in 1..d + 1{
		if roll <= n{
			let sum_left: u32 = n - roll;
			let result: u32;
			if sum_left == 0{
				result = 1;
			}
			else if cache[sum_left as usize] == 0{
				result = no_ways(sum_left, d, cache);
				cache[sum_left as usize] = result;
			}
			else{
				result = cache[sum_left as usize];
			}
			output += result;
			output %= 1e9 as u32 + 7;
		}
	}
	return output;
}

fn main(){
	let t: u8;
	let mut t_input = String::new();
	io::stdin().read_line(&mut t_input).expect("failed to read input!");
	t = t_input.trim().parse().unwrap();
	for _ in 0..t{
		let mut case_input = String::new();
		io::stdin().read_line(&mut case_input).expect("failed to read input!");
		let v: Vec<&str> = case_input.split(" ").collect();
		let n: u32 = v[0].trim().parse().unwrap();
		let d: u32 = v[1].trim().parse().unwrap();
		let mut cache: [u32; 1e5 as usize] = [0; 1e5 as usize];
		cache[1] = 1;
		println!("{}", no_ways(n, d, &mut cache));
	}
}
