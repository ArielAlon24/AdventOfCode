use std::collections::HashSet;
use std::str::FromStr;

#[derive(Debug)]
pub struct Card {
    pub id: usize,
    winning: HashSet<usize>,
    guesses: HashSet<usize>,
}

impl Card {
    pub fn points(&self) -> usize {
        2_usize.pow(self.correct().try_into().unwrap()) / 2
    }

    pub fn correct(&self) -> usize {
        self.winning
            .iter()
            .filter(|win| self.guesses.contains(&win))
            .count()
    }
}

#[derive(Debug, PartialEq, Eq)]
pub struct ParsingError;

impl FromStr for Card {
    type Err = ParsingError;

    fn from_str(line: &str) -> Result<Self, Self::Err> {
        let mut parts = line.split(": ");

        let id_part = parts.next().ok_or(ParsingError)?;
        let id = id_part
            .split_whitespace()
            .nth(1)
            .ok_or(ParsingError)?
            .parse::<usize>()
            .map_err(|_| ParsingError)?;

        let numbers_part = parts.next().ok_or(ParsingError)?;
        let mut numbers = numbers_part.split(" | ");

        let winning = numbers
            .next()
            .ok_or(ParsingError)?
            .split_whitespace()
            .map(|num| num.parse::<usize>().map_err(|_| ParsingError))
            .collect::<Result<HashSet<_>, _>>()?;

        let guesses = numbers
            .next()
            .ok_or(ParsingError)?
            .split_whitespace()
            .map(|num| num.parse::<usize>().map_err(|_| ParsingError))
            .collect::<Result<HashSet<_>, _>>()?;

        Ok(Self {
            id,
            winning,
            guesses,
        })
    }
}
