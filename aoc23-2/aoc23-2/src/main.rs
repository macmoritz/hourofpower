
fn main() {
    // let mut cups: Vec<u32> = vec![3, 8, 9, 1, 2, 5, 4, 6, 7];
    let mut cups: Vec<u32> = vec![6, 8, 5, 9, 7, 4, 2, 1, 3];
    
    for n in (*cups.iter().max().unwrap() + 1)..1000001 {
        cups.push(n as u32);
    }

    let cups_min: u32 = *cups.iter().min().unwrap();
    let cups_max: u32 = *cups.iter().max().unwrap();
    let cups_len: u32 = cups.len() as u32;
    let mut next_cup_index: u32 = 0; 
    let mut result: (Vec<u32>, u32);

    for _i in 0..10000000 {
        // println!("-- move {} --", _i + 1);
        result = make_move(cups, cups_min, cups_max, cups_len, next_cup_index);
        cups = result.0;
        next_cup_index = result.1;
    }

    // println!("\n-- final --");
    // println!("cups {:?}", cups);

    let cup_one_index = cups.iter().position(|&r| r == 1).unwrap() as usize;
    println!("next two labels on the cups after cup 1: {} * {} = {}", cups[cup_one_index + 1], cups[cup_one_index + 2], cups[cup_one_index + 1] * cups[cup_one_index + 2]);
}


fn make_move(mut cups: Vec<u32>, cups_min: u32, cups_max: u32, cups_len: u32, mut current_cup_index: u32) -> (Vec<u32>, u32) {
    let current_cup: u32 = cups[current_cup_index as usize] as u32;

    let c1 = cups.remove(((current_cup_index + 1) % cups_len) as usize);
    current_cup_index = cups.iter().position(|&r| r == current_cup).unwrap() as u32; 
    let c2 = cups.remove(((current_cup_index + 1) % (cups_len - 1)) as usize);
    current_cup_index = cups.iter().position(|&r| r == current_cup).unwrap() as u32;  
    let c3 = cups.remove(((current_cup_index + 1) % (cups_len - 2)) as usize);

    let mut destination_cup: i32 = (current_cup - 1) as i32;

    while destination_cup == c1 as i32 || destination_cup == c2 as i32 || destination_cup == c3 as i32 || destination_cup < cups_min as i32 {
        destination_cup -= 1;
        if destination_cup < cups_min as i32 {
            destination_cup = cups_max as i32;
        }
    }

    let destination_cup_index: u32 = cups.iter().position(|&r| r == destination_cup as u32).unwrap() as u32;
    cups.insert((destination_cup_index + 1) as usize, c1);
    cups.insert((destination_cup_index + 2) as usize, c2);
    cups.insert((destination_cup_index + 3) as usize, c3);

    let mut next_cup_index = cups.iter().position(|&r| r == current_cup).unwrap() as u32 + 1;
    if next_cup_index == cups_len {
        next_cup_index = 0;
    }

    (cups, next_cup_index)
}