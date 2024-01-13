import { View, Text, StyleSheet } from 'react-native'
import React from 'react'

const Footer = (props) => {
  return (
    <View style={styles.Footer}>
      <Text style={styles.Details}>
        Nhóm 3 con báo - TT_HTN - HKII_23_24
      </Text>
    </View>
  )
}

export default Footer

const styles = StyleSheet.create({
    Footer: {
        height: 84,
        width: "100%",
        backgroundColor: "#86B6F6",
        display: "flex",
        alignItems: "center",
        justifyContent: "center"
    },
    Details:{
        fontSize: 24,
        fontWeight: "600",
    },
  });
