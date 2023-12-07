use crate::card::Card;
use crate::hand_type::HandType;
use core::cmp::Ordering;

#[derive(Debug, Eq)]
pub struct Hand {
    pub cards: [Card; 5],
    pub bet: usize,
}

impl Hand {
    pub fn new(line: &str, jokers: bool) -> Result<Self, String> {
        let mut parts = line.split(" ");

        let cards: [Card; 5] = parts
            .next()
            .ok_or_else(|| "No card data found in the input".to_string())?
            .chars()
            .map(|c| Card::new(c, jokers))
            .collect::<Vec<_>>()
            .try_into()
            .map_err(|_| "Invalid number of cards, expected 5 cards".to_string())?;

        let bet: usize = parts
            .next()
            .ok_or_else(|| "No bet data found in the input".to_string())?
            .parse()
            .map_err(|_| "Couldn't parse bet.".to_string())?;

        Ok(Self { cards, bet })
    }
}

impl PartialEq for Hand {
    fn eq(&self, other: &Self) -> bool {
        self.cards == other.cards
    }
}

impl PartialOrd for Hand {
    fn partial_cmp(&self, other: &Hand) -> Option<std::cmp::Ordering> {
        let ordering = HandType::from(self).partial_cmp(&HandType::from(other));

        if ordering != Some(Ordering::Equal) {
            return ordering;
        }

        for (c1, c2) in self.cards.iter().zip(other.cards.iter()) {
            if c1 > c2 {
                return Some(Ordering::Greater);
            } else if c2 > c1 {
                return Some(Ordering::Less);
            }
        }
        None
    }
}

impl Ord for Hand {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.partial_cmp(&other).unwrap()
    }
}
