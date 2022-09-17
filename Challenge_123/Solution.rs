use std::io;

fn main(){
	// number ot test cases
	let t: u32;
	let mut t_str = String::new();
	io::stdin().read_line(&mut t_str).expect("failed to read input.");
	t = t_str.trim().parse().unwrap();
	for _ in 0..t{
		let mut case: u32;
		let mut case_str = String::new();
		io::stdin().read_line(&mut case_str).expect("failed to read input.");
		case = case_str.trim().parse().unwrap();
		while case != 1{
			print!("{} ", case);
			if case % 2 == 0{
				case /= 2;
			}
			else{
				case = case * 3 + 1
			}
		}
		println!("{}", 1)
	}
}