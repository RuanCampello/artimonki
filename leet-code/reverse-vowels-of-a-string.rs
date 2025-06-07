fn is_vowel(c: char) -> bool {
    matches!(c.to_ascii_lowercase(), 'a' | 'e' | 'i' | 'o' | 'u')
}

pub fn reverse_vowels(s: String) -> String {
    let mut chars: Vec<char> = s.chars().collect();
    let mut left = 0;
    let mut right = chars.len().saturating_sub(1);

    while left < right {
        while left < right && !is_vowel(chars[left]) {
            left += 1;
        }

        while left < right && !is_vowel(chars[right]) {
            right -= 1;
        }

        if left < right {
            chars.swap(left, right);
            left += 1;
            right -= 1;
        }
    }

    return chars.into_iter().collect();
}

fn main() {
    assert_eq!(reverse_vowels("leetcode".to_string()), "leotcede");
    assert_eq!(reverse_vowels("IceCreAm".to_string()), "AceCreIm");
}
