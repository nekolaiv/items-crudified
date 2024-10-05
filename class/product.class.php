<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
require_once "database.class.php";

class Product{
    public $id; 
    public $name;
    public $category_id;
    public $price;
    public $availability;

    protected $db;

    function __construct(){
        $this->db = new Database;
    }

    // CREATE
    function add(){
        $sql = "INSERT INTO products(code, name, category_id, price) VALUES(:code, :name, :category_id, :price)";
        $query = $this->db->connect()->prepare($sql);
        $query->bindParam(':code', $this->code);
        $query->bindParam(':name', $this->name);
        $query->bindParam(':category_id', $this->category_id);
        $query->bindParam(':price', $this->price);

        if($query->execute()){
            return true;
        } else {
            return false;
        }
    }


    // READ
    function showAll($keyword='', $category=''){
        $sql = "SELECT p.*, 
        c.name as category_name, 
        SUM(IF(s.status='in', quantity, 0)) as stock_in, 
        SUM(IF(s.status='out', quantity, 0)) as stock_out 
        FROM product p 
        INNER JOIN category c 
        ON p.category_id = c.id 
        LEFT JOIN stocks s 
        ON p.id = s.product_id 
        WHERE (p.code LIKE CONCAT('%', :keyword, '%') 
        OR p.name LIKE CONCAT('%', :keyword, '%')) 
        AND (c.id LIKE CONCAT('%', :category, '%')) 
        GROUP BY p.id ORDER BY p.name ASC;";
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
        $sql = "SELECT * FROM category ORDER BY name ASC;";
        $query = $this->db->connect()->prepare($sql);
        $data = null;
        if($query->execute()) {
            $data = $query->fetchAll(PDO::FETCH_ASSOC);
        }
        return $data;
    }

    function fetchRecord($recordID) {
        $sql = "SELECT * FROM product WHERE id = :recordID;";
        $query = $this->db->connect()->prepare($sql);
        $query->bindParam(':recordID', $recordID);
        $data = null;
        if($query->execute()) {
            $data = $query->fetch();
        }
        return $data;
    }

    function codeExists($code, $excludeID=null){
        $sql = "SELECT COUNT(*) FROM product WHERE code = :code";
        if ($excludeID){
            $sql .= " AND id != :excludeID";
        }
        $query = $this->db->connect()->prepare($sql);
        $query->bindParam(':code', $code);

        if($excludeID){
            $query->bindParam(':excludeID', $excludeID);
        }
        $query->execute();
        $count = $query->fetchColumn();

        return $count > 0;
    }

    // UPDATE
    function edit() {
        $sql = "UPDATE product SET code = :code, name = :name, category_id = :category_id, price = :price WHERE id = :id;";
        $query = $this->db->connect()->prepare($sql);
        $query->bindParam(':code', $this->code);
        $query->bindParam(':name', $this->name);
        $query->bindParam(':category_id', $this->category_id);
        $query->bindParam(':price', $this->price);
        $query->bindParam(':id', $this->id);
        return $query->execute();
    }
   
    // DELETE
    function delete($id) {
        $sql = "DELETE FROM product WHERE id = :id;";
        $query = $this->db->connect()->prepare($sql);
        $query->bindParam(':id', $id);
        return $query->execute();
    }


}
?>