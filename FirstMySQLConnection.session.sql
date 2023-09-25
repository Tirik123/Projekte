CREATE TABLE Customer (
    customer_id INT AUTO_INCREMENT NOT NULL,
    customer_first_name VARCHAR(50) NOT NULL,
    customer_last_name VARCHAR(50) NOT NULL,
    customer_treuepunkte ENUM('Ja', 'Nein') NOT NULL,
    customer_address VARCHAR(100) NOT NULL,
    customer_mail VARCHAR(80) NOT NULL,
    PRIMARY KEY (customer_id, customer_last_name)
);




CREATE TABLE Warenkorb (
    warenkorb_id INT AUTO_INCREMENT NOT NULL,
    product_name VARCHAR(150) NOT NULL,
    product_price FLOAT(10, 2) NOT NULL,
    customer_id INT NOT NULL,
    customer_last_name VARCHAR(50) NOT NULL,
    customer_treuepunkte ENUM('Ja', 'Nein') NOT NULL,
    PRIMARY KEY (warenkorb_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

