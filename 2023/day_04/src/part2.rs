mod card;

use std::collections::HashMap;
use std::fs;
use std::str::FromStr;

use crate::card::{Card, ParsingError};

fn main() -> Result<(), ParsingError> {
    let content = fs::read_to_string("input.txt").expect("Invalid File!");
    let cards: Vec<Card> = content
        .lines()
        .into_iter()
        .map(|line| Card::from_str(line))
        .collect::<Result<Vec<Card>, ParsingError>>()?;

    let mut map: HashMap<usize, usize> = HashMap::new();

    let total: usize = cards
        .iter()
        .rev()
        .map(|card| 1 + calculate_result(card.id, &cards, &mut map))
        .sum();

    println!("{:?}", total);
    Ok(())
}

fn calculate_result(id: usize, cards: &Vec<Card>, map: &mut HashMap<usize, usize>) -> usize {
    if map.contains_key(&id) {
        return *map.get(&id).unwrap();
    }
    match cards.get(id - 1) {
        None => 0,
        Some(card) => {
            let value = (0..card.correct())
                .map(|index| 1 + calculate_result(card.id + index + 1, cards, map))
                .sum();
            map.insert(id, value);
            value
        }
    }
}
