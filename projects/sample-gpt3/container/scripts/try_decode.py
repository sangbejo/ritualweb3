from web3 import Web3

web3 = Web3()


def main():
    input = "48656c6c6f2c20776861742069732032202a20333f"
    byte_array = bytes.fromhex(input)
    string_data = byte_array.decode('utf-8')

    print(string_data)  # Output: 'hello'


if __name__ == "__main__":
    main()
