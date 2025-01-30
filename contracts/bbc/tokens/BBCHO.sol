// BBCHO.sol
pragma solidity ^0.8.0;

contract BBCHO {
    string public name = "Token BBCHO";
    string public symbol = "BBCHO";
    uint8 public decimals = 18;
    uint256 public totalSupply = 750000 * (10 ** uint256(decimals));
    mapping(address => uint256) public balanceOf;

    constructor() {
        balanceOf[msg.sender] = totalSupply;
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance.");
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        return true;
    }
}
