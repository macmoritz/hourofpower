use std::collections::LinkedList;
use std::collections::HashMap;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn main() {
    let moves: HashMap<&str, (i32, i32)> =
        [("e", (1, 0)),
        ("w", (-1, 0)),
        ("ne", (1, -1)),
        ("nw", (0, -1)),
        ("se", (0, 1)),
        ("sw", (-1, 1))].iter().cloned().collect();

    let mut black_tiles: LinkedList<(i32, i32)> = LinkedList::new();

    let file = File::open("./../input.txt").unwrap();
    let content = BufReader::new(&file);
    let size: i32 = 84;
    let mut tile: (i32, i32);
    let mut next_move: (i32, i32) = (0, 0);

    for line in content.lines() {
        tile = (size, size);
        let mut path = line.unwrap();
        while path.chars().count() > 0 {
            if moves.contains_key(&path.get(0..1).unwrap()) {
                next_move = *moves.get(&path.get(0..1).unwrap()).unwrap();
                path = path.get(1..path.chars().count()).unwrap().to_string();
            } else if moves.contains_key(&path.get(0..2).unwrap()) {
                next_move = *moves.get(&path.get(0..2).unwrap()).unwrap();
                path = path.get(2..path.chars().count()).unwrap().to_string();
            }
            tile.0 += next_move.0;
            tile.1 += next_move.1;
        }

        if black_tiles.contains(&tile) {
            let remove_index = black_tiles.iter().position(|&x| x == tile).unwrap() as usize;
            let mut split_list = black_tiles.split_off(remove_index);
            split_list.pop_front();
            black_tiles.append(&mut split_list);
        } else {
            black_tiles.push_back(tile);
        }
    }

    println!("-- {} tiles flipped --", black_tiles.len());
}
