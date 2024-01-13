import { StyleSheet, View, Platform, Dimensions  } from 'react-native';
import Home from './src/pages/Home';
import {Header, Footer} from './src/navs/master'

export default function App() {
  console.log("start",Platform.OS === "ios" ? "ios" : "android", Dimensions. get('window'))
  const styles = StyleSheet.create({
    container: {
      width: Dimensions. get('window')["width"],
      height: Dimensions. get('window')["height"],
      backgroundColor: "#EEF5FF",
      display:"flex",
    },
  });
  return (
    <View style={styles.container}>
      <Header/>
      <Home/>
      <Footer/>
    </View>
  );
}
