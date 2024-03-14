import React, { useEffect, useState } from "react";
import { View, Text, StyleSheet, ScrollView, FlatList } from "react-native";
import { db } from "../configs/firebaseConfig";
import { onValue, ref } from "firebase/database";
const Home = (props) => {
  const [numEmpty, numEmptySet] = useState(0);
  const [listEmpty, listEmptySet] = useState([]);
  const [listDataSlot, listDataSlotSet] = useState([]);

  const styles = StyleSheet.create({
    home: {
      flex: 1,
      // width: props.Dimensions.width,
      // display: "flex",
      // flexDirection: 'column',
      justifyContent: 'center',
      alignItems:'center',
      // paddingLeft:20
    },
    container: {
      flexDirection: 'row',
      flexWrap: 'wrap',
      justifyContent: 'flex-end',
    },
    item: {
      alignItems: 'center',
      justifyContent: 'center',
      width: '26%',
      aspectRatio: 1.1,
      marginVertical: 4,
      marginHorizontal: '1.4%',
    },
    title: {
      fontSize: 10,
    },
    textSlot:{
      fontSize: 20,
    }
  });

  const renderItem = ({ item }) => (
    <View style={{backgroundColor:item.split("-")[2] === "None" ? "green" : "red",...styles.item}}>
      <Text style={styles.title}>{item.split("-")[0] + item.split("-")[1]}</Text>
      <Text style={styles.title}>ID: {item.split("-")[2] !== "None" ? item.split("-")[2].split(",")[0]: "Còn Trống"}</Text>
      <Text style={styles.title}>{item.split("-")[2] !== "None" ? item.split("-")[2].split(",")[1]: ""}</Text>
    </View>
  );

  useEffect(() => {
    const intervalId = setInterval(() => {
      const data = ref(db, "lineSlot");
      onValue(data, (snapshot) => {
        const data = snapshot.val();
        const data_empty_slot = data["empty_slot"];
        const data_num_empty_slot = data_empty_slot[0];
        const list_empty_slot = data_empty_slot[1];
        const data_list_slot = data["list_slot"];
        numEmptySet(data_num_empty_slot);
        listEmptySet(list_empty_slot);
        listDataSlotSet(data_list_slot);
      });
    }, 5000);
    return () => clearInterval(intervalId);
  }, []);

  return (
    <View style={styles.home}>
      <Text style={styles.textSlot}>
        Số lượng vị trí trống: {numEmpty}
      </Text>
      <FlatList
        data={listDataSlot}
        renderItem={renderItem}
        keyExtractor={(item, index) => index.toString()} // Assuming each item has unique index
        numColumns={3}
        contentContainerStyle={styles.container}
      />
    </View>
  )
};

export default Home;
