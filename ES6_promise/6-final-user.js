import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, filename) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(filename)])
    .then((values) => {
      const rejected = values.filter((value) => value.status === 'rejected');
      const fulfilled = values.filter((value) => value.status === 'fulfilled');
      fulfilled.forEach((value) => console.log(`${value.value.firstName} ${value.value.lastName}`));
      rejected.forEach((value) => console.log(value.reason.message));
    });
}
