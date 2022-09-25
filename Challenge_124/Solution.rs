use std::io;

fn sum_of_squares(num: i64) -> i64{
	return (num * (num + 1) * (2 * num + 1) / 6) % (10i64.pow(9) + 7);
}

fn main(){
	let t: i64;    // number of test cases
	let mut t_input = String::new();
	io::stdin().read_line(&mut t_input).expect("failed to read input!");
	t = t_input.trim().parse().unwrap();
	for _i in 0..t{
		let mut case = String::new();
		io::stdin().read_line(&mut case).expect("failed to read input!");
		let v: Vec<&str> = case.split(' ').collect();
		let start: i64 = v[0].trim().parse().unwrap();
		let end: i64 = v[1].trim().parse().unwrap();
		if sum_of_squares(end) - sum_of_squares(start - 1) < 0{
			println!("{}", sum_of_squares(end) - sum_of_squares(start - 1) + (10i64.pow(9) + 7));
		}
		else{
			println!("{}", sum_of_squares(end) - sum_of_squares(start - 1));
		}
	}
}