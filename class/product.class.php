<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
require_once "database.class.php";

class Product{
    public $id; 
    public $name;
    public $category;
    public $price;
    public $availability;

    protected $db;

    function __construct(){
        $this->db = new Database;
    }

    // CREATE
    function add(){
        $sql = "INSERT INTO products(name, category, price, availability) VALUES(:name, :category, :price, :availability)";
        $query = $this->db->connect()->prepare($sql);
        $query->bindParam(':name', $this->name);
        $query->bindParam(':category', $this->category);
        $query->bindParam(':price', $this->price);
        $query->bindParam(':availability', $this->availability);

        if($query->execute()){
            return true;
        } else {
            return false;
        }
    }

    // READ 
    function showAll(){
        $sql = "SELECT * FROM products";
        $query = $this->db->connect()->prepare($sql);
        $data=null;
        if($query->execute()){
            $data = $query->fetchAll();
        }
        return $data;
    }

    function showAllSearched($keyword, $category){
        $sql =  "SELECT * FROM products WHERE name LIKE '%' :keyword '%' AND category LIKE '%' :category '%' ORDER BY name ASC;";
        $query = $this->db->connect()->prepare($sql);
        $query->bindParam(':keyword', $keyword);
        $query->bindParam(':category', $category);
        $data=null;
        if($query->execute()){
            $data = $query->fetchAll();
        }
        return $data;
    }

    function fetchCategory() {
        $sql = "SELECT DISTINCT category FROM products ORDER BY category ASC;";
        $query = $this->db->connect()->prepare($sql);
        $data = null;
        if($query->execute()) {
            $data = $query->fetchAll();
        }
        return $data;
    }

    function fetchRecord($recordID) {
        $sql = "SELECT * FROM products WHERE id = :recordID;";
        $query = $this->db->connect()->prepare($sql);
        $query->bindParam(':recordID', $recordID);
        $data = null;
        if($query->execute()) {
            $data = $query->fetch();
        }
        return $data;
    }

    // UPDATE
    function edit() {
        $sql = "UPDATE products SET name = :name, category = :category, price = :price, availability = :availability WHERE id = :id;";
        $query = $this->db->connect()->prepare($sql);
        $query->bindParam(':name', $this->name);
        $query->bindParam(':category', $this->category);
        $query->bindParam(':price', $this->price);
        $query->bindParam(':availability', $this->availability);
        $query->bindParam(':id', $this->id);
        return $query->execute();
    }
   
    // DELETE
    function delete($id) {
        $sql = "DELETE FROM products WHERE id = :id;";
        $query = $this->db->connect()->prepare($sql);
        $query->bindParam(':id', $id);
        return $query->execute();
    }
}
?>