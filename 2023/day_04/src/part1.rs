mod card;

use std::fs;
use std::str::FromStr;

use crate::card::{Card, ParsingError};

fn main() -> Result<(), ParsingError> {
    let sum: usize = fs::read_to_string("input.txt")
        .expect("Invalid File!")
        .lines()
        .filter_map(|line| Card::from_str(line).ok())
        .map(|card| card.points())
        .sum();

    println!("{:?}", sum);

    Ok(())
}
