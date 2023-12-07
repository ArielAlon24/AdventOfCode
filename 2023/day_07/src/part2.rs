use crate::hand::Hand;
use crate::hand_type::HandType;
use std::fs;

mod card;
mod hand;
mod hand_type;

fn main() {
    let content = fs::read_to_string("input.txt").expect("Invalid File!");

    let mut hands: Vec<_> = content
        .split("\n")
        .map(|line| {
            let hand = Hand::new(line, true).unwrap();
            println!("{line} -> {:?}", HandType::from(&hand));
            hand
        })
        .collect();

    let mut sum = 0;
    hands.sort();
    for (index, hand) in hands.iter().enumerate() {
        sum += (index + 1) * hand.bet;
    }

    println!("{sum:?}")
}
