use std::env;
use std::fs::File;
use std::io::{Read};

fn find_loop_size(publickey: u64) -> u64 {
    let mut value: u64 = 1;
    let mut loops: u64 = 0;
    while value != publickey {
        value = (value * 7) % 20201227;
        loops += 1;
    }
    loops
}

fn transform(subject: u64, n: u64) -> u64 {
    let mut value = 1;
    for _ in 0..n {
        value = (subject * value) % 20201227;
    }
    value
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let mut file = File::open(&args[1]).unwrap();
    let mut content = String::new();
    file.read_to_string(&mut content);
    let split_lines: Vec<&str> = content.trim().split("\n").collect();

    let door_public_key: u64 = split_lines[0].parse().unwrap();
    let card_public_key: u64 = split_lines[1].parse().unwrap();

    let card_loop_size: u64 = find_loop_size(card_public_key);
    let door_loop_size: u64 = find_loop_size(door_public_key);

    let encryption_key_1: u64 = transform(door_public_key, card_loop_size);
    let encryption_key_2: u64 = transform(card_public_key, door_loop_size);

    if encryption_key_1 == encryption_key_2 {
        println!("encrytion key is {}", encryption_key_1)
    }
}
