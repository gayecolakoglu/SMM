INSERT INTO difficulty (difficulty_id,difficulty_type)
VALUES (1, 'easy'),(2,'normal'),(3,'expert'),(4,'superExpert');

INSERT INTO game_play_properties_type (type_id,type_name)
VALUES (1, 'plays'),(2,'likes'),(3,'clears'),(4,'records');

INSERT INTO style (style_id,style_name)
VALUES (1, 'marioBros3'),(2,'marioBrosU'),(3,'marioWorld');

UPDATE players
SET player_name = CONCAT(LEFT(player_name, CHAR_LENGTH(player_name) -1), '');

load data
infile "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\players_id.csv"
into table players
columns terminated  by '\t';

load data
infile "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\allQuadra_write.csv"
into table game_play_properties
columns terminated  by '\t'
(m_id,p_id,catch,@VAL,properties_type_id)
    set record=if(@VAL ="", null, @VAL);

show variables like "secure_file_priv";


ALTER TABLE game_play_properties DROP PRIMARY KEY, ADD PRIMARY KEY(m_id, p_id, properties_type_id);
ALTER TABLE course_meta
DROP clear_rate;

#stored procedure
DELIMITER //
CREATE  PROCEDURE `clearRate`(IN clear_number INT,IN attemp_number INT,OUT clear_rate FLOAT)
BEGIN
set clear_rate=(clear_number/attemp_number)*100;
END //
DELIMITER ;

DELIMITER //
CREATE  PROCEDURE `get_player_name`(INOUT player varchar(45))
BEGIN
select player_name into player
from players
where player=player_id;
END //
DELIMITER ;

set @a=0;
set@b=0;
select clears_num,attemps_num into @a,@b
from course_meta
where catch=20171116144536703;
call clearRate(@a,@b,@c);
select @c;
select@a;
select@b;

set @d="gotatari";
call get_player_name(@d);
select @d;

#view
create view clear_rate  as
select clears_num,attemps_num,((clears_num/attemps_num)*100)as clear_Rate
from course_meta;
