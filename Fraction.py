class Fraction:
    def __init__(this, numerator, denominator):
        this.numerator = numerator
        this.denominator = denominator
    
    def simplify(this):
        gcd = math.gcd(this.numerator, this.denominator)
        this.numerator = this.numerator / gcd
        this.denominator = this.denominator / gcd
    
    def double(this):
        this.numerator = this.numerator * 2

    def square(this):
        this.numerator = this.numerator * this.numerator
        this.denominator = this.denominator * this.denominator

    def inverse(this):
        this.denominator, this.numerator = this.numerator, this.denominator

    def minus_one(this):
        this.numerator = this.numerator - this.denominator

