use crate::card::Card;
use crate::Hand;
use std::collections::HashMap;

#[derive(PartialEq, Debug)]
pub enum HandType {
    FiveOfAKind,
    FourOfAKind,
    FullHouse,
    ThreeOfAKind,
    TwoPair,
    OnePair,
    HighCard,
}

impl From<&HandType> for usize {
    fn from(hand_type: &HandType) -> Self {
        match hand_type {
            HandType::FiveOfAKind => 7,
            HandType::FourOfAKind => 6,
            HandType::FullHouse => 5,
            HandType::ThreeOfAKind => 4,
            HandType::TwoPair => 3,
            HandType::OnePair => 2,
            HandType::HighCard => 1,
        }
    }
}

impl PartialOrd for HandType {
    fn partial_cmp(&self, other: &HandType) -> Option<std::cmp::Ordering> {
        usize::from(self).partial_cmp(&usize::from(other))
    }
}

impl From<&Hand> for HandType {
    fn from(hand: &Hand) -> Self {
        let mut counter = HashMap::new();
        let mut jokers = 0;
        for card in &hand.cards {
            if card == &Card::Joker {
                jokers += 1;
            } else {
                *counter.entry(card).or_insert(0) += 1;
            }
        }

        let mut values = counter.values().collect::<Vec<_>>();
        values.sort();
        values.reverse();

        match (jokers, values.as_slice()) {
            (n, [m, ..]) if *m + n == 5 => HandType::FiveOfAKind,
            (n, [m, ..]) if *m + n == 4 => HandType::FourOfAKind,
            (n, [3, m, ..]) if *m + n == 2 => HandType::FullHouse,
            (1, [2, 2, ..]) => HandType::FullHouse,
            (n, [m, ..]) if *m + n == 3 => HandType::ThreeOfAKind,
            (n, [m1, m2, ..]) if *m1 <= &2 && *m2 <= &2 && *m1 + *m2 + n == 4 => HandType::TwoPair,
            (n, [m, ..]) if *m + n == 2 => HandType::OnePair,
            _ => HandType::HighCard,
        }
    }
}
