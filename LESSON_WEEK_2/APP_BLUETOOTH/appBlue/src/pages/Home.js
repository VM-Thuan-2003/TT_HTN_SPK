import React from 'react'
import { StyleSheet, Text, View } from 'react-native';

const Home = (props) => {
    const styles = StyleSheet.create({
        Home: {
            width: "100%",
            height: "auto",
            display: "flex",
            flexGrow: 1,
            justifyContent: "center",
            alignItems: "center"
        },
        });
    return (
        <View style={styles.Home}>
            <Text>
                This is a page Home
            </Text>
        </View>
    )
}

export default Home