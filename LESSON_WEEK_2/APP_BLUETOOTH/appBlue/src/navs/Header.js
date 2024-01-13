import { View, Text, StyleSheet, Pressable} from 'react-native'
import React from 'react'
const Header = (props) => {
    
  return (
    <View style={styles.Header}>
        <Pressable style={styles.Btn} onPress={()=>{console.log("sss")}}>
            <Text>
                List Connect
            </Text>
        </Pressable>
        <Text style={styles.Info}>
            APP - CONTROL - BLUETOOTH
        </Text>
    </View>
  )
}

export default Header

const styles = StyleSheet.create({
    Header: {
        height: 98,
        width: "100%",
        backgroundColor: "#86B6F6",
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "space-between"
    },
    Info:{
        fontSize: 20,
        paddingRight:20,
    },
    Btn:{
        marginLeft: 20,
        padding: 8,
        fontSize: 20,
        backgroundColor: "#D9EDBF",
        borderRadius:10,
        color: "black",
        fontWeight: "600",
    },
  });