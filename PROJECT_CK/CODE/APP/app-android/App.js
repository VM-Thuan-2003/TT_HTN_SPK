import { StatusBar } from 'expo-status-bar';
import { StyleSheet, View, Dimensions } from 'react-native';

import Home from './components/pages/Home';
import Header from './components/layouts/Header';
import Footer from './components/layouts/Footer';

export default function App() {
  const { width, height } = Dimensions.get('window');

  const styles = StyleSheet.create({
    container: {
      height: height,
      width: width,
      flexDirection : 'column',
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'center',
    },
  });

  return (
    <View style={styles.container}>
      <Header Dimensions={{ width, height }} />
      <Home Dimensions={{ width, height }}/>
      <Footer Dimensions={{ width, height }}/>
      <StatusBar style="auto" />
    </View>
  );
}