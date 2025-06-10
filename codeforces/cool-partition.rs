use std::collections::HashSet;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let t = lines.next().unwrap()?.parse::<usize>().unwrap();

    (0..t).for_each(|_| {
        let _ = lines.next();
        let line = lines.next().unwrap().unwrap();
        let ans = line
            .split_whitespace()
            .filter_map(|s| s.parse::<usize>().ok())
            .fold(
                (HashSet::new(), HashSet::new(), 0),
                |(mut cur, mut seen, count), x| {
                    cur.insert(x);
                    seen.insert(x);
                    match cur.len() == seen.len() {
                        true => {
                            seen.clear();
                            (cur, seen, count + 1)
                        }
                        false => (cur, seen, count),
                    }
                },
            )
            .2;

        println!("{}", ans);
    });

    Ok(())
}

