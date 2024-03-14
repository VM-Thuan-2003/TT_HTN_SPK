import React from 'react';
import { View, Text, StyleSheet, Image } from 'react-native';

const Footer = (props) => {
    const styles = StyleSheet.create({
        footer: {
            width:props.Dimensions.width,
            height:(props.Dimensions.height*20)/100,
            backgroundColor: "#f2f2f2",
            display: "flex",
            flexDirection:"column",
            alignItems: "center",
            justifyContent: "center",
        },
        footerText: {
          fontSize: 14,
          color: '#666',
        },
        footerLogo:{
            width:80,
            height:80,
            marginBottom:10
        }
      });
  return (
    <View style={styles.footer}>
      <Image
        style={styles.footerLogo}
        source={require('../static/imgs/logo.png')}
      />
      <Text style={styles.footerText}>© 2024 App-Parking-Slot. Nhóm 3 con báo.</Text>
    </View>
  );
};



export default Footer;
