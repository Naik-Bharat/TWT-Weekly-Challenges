use std::io;

fn main(){
	let mut t = String::new();
	io::stdin().read_line(&mut t).expect("Failed to read input!");
	let t: u32 = t.trim().parse().expect("Failed to convert to string");
	for _ in 0..t{
		let mut case = String::new();
		io::stdin().read_line(&mut case).expect("Failed to read input!");
		case = case.trim().to_string();
		let mut curr_count: u32 = 0;
		let mut max_count: u32 = 0;
		for character in case.chars(){
			if character == 'A'{
				curr_count += 1;
				if max_count < curr_count{
					max_count = curr_count;
				}
			}
			else{
				curr_count = 0;
			}
		}
		println!("{}", max_count);
	}
}
