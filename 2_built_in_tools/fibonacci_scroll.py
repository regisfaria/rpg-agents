
# ✨🧙 The Ancient Scroll of Fibonacci ✨
# Inscribed by Kiro the Grey Hat
# This spell summons the sacred sequence of Fibonacci!

def cast_fibonacci_spell(n):
    """
    🔮 A mystical spell that conjures the first n numbers
    of the legendary Fibonacci sequence!
    """
    print("=" * 45)
    print("  ✨ THE FIBONACCI CONJURATION BEGINS ✨")
    print("=" * 45)

    sequence = []
    a, b = 0, 1

    for i in range(n):
        sequence.append(a)
        a, b = b, a + b  # 🌀 The magic transformation!

    print(f"\n🔮 Summoning the first {n} Fibonacci numbers...\n")

    for idx, num in enumerate(sequence):
        stars = "⭐" * (idx + 1)
        print(f"  [{idx + 1:>2}]  {num:>5}  {stars}")

    print("\n" + "=" * 45)
    print(f"  🧙 Spell complete! Sequence summoned:")
    print(f"  {sequence}")
    print("=" * 45)
    return sequence

# 🪄 Cast the spell for the first 10 numbers!
cast_fibonacci_spell(10)
