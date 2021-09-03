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

    let mut current_tile: (i32, i32);
    let mut copy: LinkedList<(i32, i32)>;
    let mut black_neighbours_count: i32;

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

    for day in 0..100 {
        copy = black_tiles.clone();

        for i in 0..(size * 2) {
            for j in 0..(size * 2) {
                current_tile = (i, j);
                black_neighbours_count = get_black_neighbours_count(current_tile, &moves, &black_tiles);

                if black_tiles.contains(&current_tile) {
                    if black_neighbours_count == 0 || black_neighbours_count > 2 {
                        let remove_index = copy.iter().position(|&x| x == current_tile).unwrap() as usize;
                        let mut split_list = copy.split_off(remove_index);
                        split_list.pop_front();
                        copy.append(&mut split_list);
                    }
                } else {
                    if black_neighbours_count == 2 {
                        copy.push_back(current_tile);
                    }
                }
            }
        }
        black_tiles = copy;
        println!("Day {}: {}", day + 1, black_tiles.len());
    }

    println!("-- {} tiles flipped --", black_tiles.len());
}

fn get_black_neighbours_count(tile: (i32, i32), moves: &HashMap<&str, (i32, i32)>, black_tiles: &LinkedList<(i32, i32)>) -> i32 {
    let mut count: i32 = 0;
    for (_key, value) in moves.into_iter() {
        let neighbour: (i32, i32) = (tile.0 + value.0, tile.1 + value.1);
        if black_tiles.contains(&neighbour){
            count += 1;
        }
    }
    count
}
