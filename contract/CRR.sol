// SPDX-License-Identifier: MIT

pragma solidity ^0.8.4;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

import "./ERC721A.sol";

contract CRR is
    ERC721A,
    Ownable,
    ReentrancyGuard,
{
    using ECDSA for bytes32;

    uint256 public constant MAX_SUPPLY = 5000;

    uint256 public salePrice = 0.001 ether;

    bool private hasOwnerMint;

    constructor() ERC721A("Crazy Rich Rabbit", "CRR") {}

    modifier onlyEOA() {
        require(tx.origin == msg.sender, "Contracts not allowed");
        _;
    }

    //  Set Sale Price
    function setSalePrice(uint256 price) external onlyOwner {
        salePrice = price;
    }

    //  owner mint
    function OwnerMint() external payable onlyOwner {
        require(hasOwnerMint != true, "Already Owner Mint");
        _safeMint(msg.sender, 1);
        hasOwnerMint = true;
    }

    // Public Sale
    function PublicSalesMint(uint256 qty)
        external
        payable
        nonReentrant
        onlyEOA
    {
        require(qty != 0, "Public Sale: No Quantity");
        require(
            totalSupply() + qty <= MAX_SUPPLY,
            "Public Sale: Over Max Supply"
        );
        require(msg.value >= salePrice * qty, "Public Sale: Insufficient ETH");

        _safeMint(msg.sender, qty);
    }

    // // metadata URI
    string private baseTokenURI;

    function _baseURI() internal view virtual override returns (string memory) {
        return baseTokenURI;
    }

    function setBaseURI(string calldata baseURI) external onlyOwner {
        baseTokenURI = baseURI;
    }

    //  Withdraw ETH
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "Withdraw: Insufficient ETH");
        (bool success, ) = payable(msg.sender).call{value: balance}("");
        require(success, "Withdraw: Failed");
    }
}
