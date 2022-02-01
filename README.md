# SMM

This Project consist on dataset of super mario maker the dataset downloaded via [kaggle](https://www.kaggle.com/leomauro/smmnet). In this project, an ER diagram was created, then the cleaned data was edited according to the ER diagram, and then the data was loaded into the relevant tables with MySQL Workbench and Visual Studio Code. In addition, a basic GUI was created that can connect to the database, retrieve data and display this data using python's tkinter library.

You can see the GUI below:

![image](https://user-images.githubusercontent.com/55553433/151961371-409c7241-5530-4666-856f-b1c7b8ad50cf.png) ![image](https://user-images.githubusercontent.com/55553433/151961383-661407d3-f3ed-42ed-a261-929c7be22baa.png)



## Creating ER Diagram
First of all we changed ER diagram design so that it can be 3NF form.We add difficulty , style,game_play_properties_type and game_play_properties tables then we drop plays,clears,likes,records tables.Secondly we add columns p_id and m_id to players and courses tables because we need int primary key  ,otherwise varchar will be slower.Finally we drop clear_rate column from course_meta table because we can find it by using clear number and attempts number.

Since we have big datas when we run a query we can see that primary keys repeats at the output.We can create an ER diagram which is more efficient ,so that we can decrease the repetition of primary keys.


## Loadind Data
I download all dataset from kaggle.But it was not enough because dataset’s form were not in the proper shape for our ER diagram.So ı write several python codes that edits all datasets into proper form then load this datas to the MySQL.

  - I uploeded all data except the clear_rate column from course_meta table because we can find the clear rate from clear number and attempts number 

  - I used MySql Workbench for only one table ,for other table ı used Visual Studio Code/Python.



## Stored Procedures & Views
We have two stored procedure and one view.

  1)	clearRate(@a,@b,@c) .This stored procedure calculates the clear rate by using a=clears_num,b=attemps_num and returns c=output.
  2)	Get_player_name(@d) .This stored procedure get player name by using d=player_id and returns d=output.
  3)	clear_rate.This view returns 3 columns: clears_num,attemps_num (from course_meta) and clear_Rate. (by calculating it from clears_num and attemps_num)

  Here you can see the view example(clear_rate):
  
  ![image](https://user-images.githubusercontent.com/55553433/151961509-48aa9713-9923-4d38-8ab2-7fcc35969589.png)



- You can use the [exportCode](https://github.com/gayecolakoglu/SMM/tree/main/exportCode) link to export relevant data.

- You can use [GUI](https://github.com/gayecolakoglu/SMM/tree/main/GUI) link to reach GUI codes.

- You can use the [editCodes](https://github.com/gayecolakoglu/SMM/tree/main/editCodes) link to access the codes where the downloaded data is cleaned and arranged to fit the ER diagram.

- You can also use [ER](https://github.com/gayecolakoglu/SMM/tree/main/ER) link to reach the relevant ER diagram.


