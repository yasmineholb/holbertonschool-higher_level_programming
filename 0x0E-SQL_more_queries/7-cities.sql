-- task 7
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
  id int NOT NULL AUTO_INCREMENT,
  state_id int NOT NULL,
  name varchar(256) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT FK_state_id FOREIGN KEY (state_id) REFERENCES states(id)
);